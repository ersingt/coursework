import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
import cufflinks

setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)

df_iris = px.data.iris()
# df_iris

st.header("Plotly Demo")

# fig = px.scatter(
#     df_iris,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     marginal_y="rug",
#     marginal_x="histogram",
# )

# fig.update_layout(title="Plot Title", xaxis_title="x Axis Title")

# fig

# # what_is_fig = type(fig)
# # what_is_fig

# # my_bar = px.bar(df_iris, x='sepal_width', y='sepal_length', title="width and length")
# # my_bar


# # my_bar.data[0].update(
# #     text=df_iris['sepal_length'],
# #     textposition=('inside'),
# # )
# # my_bar

# df = pd.DataFrame(np.random.rand(6, 3), columns=['A', 'B', 'C'])

# # .iplot() is part of cufflinks api
# # df.iplot(kind='bar', )

# fig.write_html("example_plot.html")


df_geo = px.data.gapminder()

geo_fig = px.scatter_geo(
    df_geo,
    locations="iso_alpha",
    color="continent",
    hover_name="country",
    size="pop",
    animation_frame="year",
    projection="sinusoidal",
)
geo_fig
