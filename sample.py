#%%
import altair as alt
from vega_datasets import data

cars = data.cars()
brush = alt.selection(type='interval')

car_chart = alt.Chart(cars).mark_circle(size=60).encode(
                x='Horsepower',
                y='Miles_per_Gallon',
                color=alt.condition(brush, 'Origin', alt.ColorValue('gray')),
                tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
            ).add_selection(
                    brush
        ).properties(
            width=250,
            height=250
        )

car_chart
# %%
