import streamlit as st
from openai import OpenAI
import re

client = OpenAI(api_key="chatgpt API") # Use your own Api key

st.title("Food Recipe and Ingredient Cost Calculator")

food_name = st.text_input("Enter the name of the dish:")

if food_name:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides recipes and ingredient lists. Format the response with ingredients in the format: 'Quantity Ingredient - $Cost'. For example: '2 cups Rice - $1.50'."},
                {"role": "user", "content": f"Provide a detailed recipe and list of ingredients for {food_name}. Also, provide an estimated cost for each ingredient in USD."}
            ]
        )
        recipe_response = response.choices[0].message.content
        
        st.subheader(f"Recipe for {food_name}:")
        st.write(recipe_response)

        ingredient_cost_pattern = re.compile(r"(\d+\s?\w+)\s([\w\s]+)\s-\s\$([\d\.]+)")
        ingredients = ingredient_cost_pattern.findall(recipe_response)

        if ingredients:
            st.subheader("Ingredients and Costs:")
            for i, (quantity, ingredient, cost) in enumerate(ingredients):
                col1, col2, col3 = st.columns(3)
                with col1:
                    new_quantity = st.text_input(f"Quantity {i+1}", value=quantity, key=f"qty_{i}")
                with col2:
                    new_ingredient = st.text_input(f"Ingredient {i+1}", value=ingredient, key=f"ing_{i}")
                with col3:
                    new_cost = st.number_input(f"Cost {i+1}", value=float(cost), key=f"cost_{i}")
                
                ingredients[i] = (new_quantity, new_ingredient, new_cost)

            st.subheader("Add New Ingredient")
            new_qty = st.text_input("Quantity", key="new_qty")
            new_ing = st.text_input("Ingredient", key="new_ing")
            new_cost = st.number_input("Cost", key="new_cost")

            if st.button("Add Ingredient"):
                if new_qty and new_ing and new_cost:
                    ingredients.append((new_qty, new_ing, new_cost))
                    st.success("Ingredient added!")

            st.subheader("Remove Ingredient")
            remove_index = st.number_input("Enter the index of the ingredient to remove", min_value=0, max_value=len(ingredients)-1, step=1)
            if st.button("Remove Ingredient"):
                if 0 <= remove_index < len(ingredients):
                    ingredients.pop(remove_index)
                    st.success("Ingredient removed!")

            total_cost = sum(float(cost) for _, _, cost in ingredients)
            st.subheader(f"Total Cost: ${total_cost:.2f}")

            if st.button("Update Recipe"):
                updated_recipe = f"Updated Recipe for {food_name}:\n\n"
                for qty, ing, cost in ingredients:
                    updated_recipe += f"{qty} {ing} - ${cost}\n"
                st.write(updated_recipe)

    except Exception as e:
        st.error(f"An error occurred: {e}")