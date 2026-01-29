from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

def Dash_board(df):  
    df = df.copy()

    # Clean 'salary' column
    if 'salary' in df.columns:
        df['salary'] = (
            df['salary']
            .astype(str)
            .str.replace('[₹$,]', '', regex=True)
            .str.extract('(\d+)')[0]
            .astype(float)
        )
    
    # Clean 'company_size' column
    if 'company_size' in df.columns:
        df['company_size'] = (
            df['company_size']
            .astype(str)
            .str.extract('(\d+)')[0]
            .astype(float)
        )

    # Clean 'revenue' column
    if 'revenue' in df.columns:
        df['revenue'] = (
            df['revenue']
            .astype(str)
            .str.replace('[₹$,]', '', regex=True)
            .str.extract('(\d+)')[0]
            .astype(float)
        )

    # Select numeric columns to display
    numeric_columns = ['salary', 'company_size', 'revenue']
    available_columns = [col for col in numeric_columns if col in df.columns]

    if not available_columns:
        print("No numeric columns available for dashboard.")
        return

    # Fill missing numeric values with 0
    df[available_columns] = df[available_columns].fillna(0)

    app = Dash(__name__)

    # Layout
    app.layout = html.Div([
        html.H1("Statistics Dashboard", style={'textAlign': 'center', 'color': '#003366'}),

        dcc.Dropdown(
            id="metric_dropdown",
            options=[{"label": col.replace("_"," ").title(), "value": col} for col in available_columns],
            value=available_columns[0],
            clearable=False,
            style={'width': '50%', 'margin': '10px auto', 'fontSize': 16}
        ),

        dcc.Graph(
            id="metric_graph",
            style={"width": "90%", "height": "60vh", "margin": "auto"}
        )
    ], style={'backgroundColor': "#ffffff", 'padding': '20px'})

    # Callback
    @app.callback(
        Output("metric_graph", "figure"),
        Input("metric_dropdown", "value")
    )
    def update_graph(selected_metric):
        if selected_metric not in df.columns:
            return px.bar(title=f"No data available for {selected_metric}")

        # Use 'job_title' for x-axis if exists, otherwise index
        x_axis = 'job_title' if 'job_title' in df.columns else df.index

        fig = px.bar(
            df,
            x=x_axis,
            y=selected_metric,
            title=f"{selected_metric.replace('_',' ').title()} Distribution",
            labels={x_axis: "Job Title" if x_axis=='job_title' else "Index", "y": selected_metric.replace("_"," ").title()},
            hover_data=df.columns
        )

        fig.update_layout(
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#ffffff",
            font=dict(color="#000000", size=14),
            title_font_size=20,
            xaxis_tickangle=-45
        )

        return fig

    app.run(debug=False)
