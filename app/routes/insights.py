import pandas as pd
import plotly.express as px
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

# Set up router and templates
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Define the file path for the CSV file
CSV_PATH = os.path.join("app", "static", "sheets","mission_climate_cues.csv")

#app\static\sheets\mission_climate_cues.csv

@router.get("/insights", response_class=HTMLResponse)
async def insights(request: Request):
    # Read CSV file
    df = pd.read_csv(CSV_PATH)

    # Clean the data by stripping any extra whitespace or newlines
    df.columns = df.columns.str.strip()


    '''
    # First Bar Chart: Climate Change Effects Awareness
    counts = df['Have  you heared about the following incidents? (Select all that apply)'].value_counts()
    bar_chart = px.bar(
        x=counts.values,
        y=counts.index,
        orientation='h',
        labels={'x': 'Count', 'y': 'Climate Change Effects'},
        #title='Which of the following climate change effects are you aware of?',
        template='plotly'
    )
    # Create a JSON representation of the chart for rendering in the template
    # Disable the legend
    bar_chart.update_layout(showlegend=False)
    bar_chart_html = bar_chart.to_html(full_html=False) 
    
    '''

    # Second Pie Chart: Are you experiencing any effects of climate change in your area?
    pie_data = df['Are you experiencing any effects of Climate Change in your area?'].value_counts()
    pie_chart = px.pie(
        names=pie_data.index,
        values=pie_data.values,
        #title="Are you experiencing any effects of Climate Change in your area?",
        template='plotly',
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    # Create a JSON representation of the chart for rendering in the template
    pie_chart.update_layout(showlegend=False)
    pie_chart_html = pie_chart.to_html(full_html=False)

    # Third Pie Chart: Are you experiencing any effects of climate change in your area?
    pie_data2 = df['How much do you know about carbon offsets?'].value_counts()
    pie_chart2 = px.pie(
        names=pie_data2.index,
        values=pie_data2.values,
        #title="Are you experiencing any effects of Climate Change in your area?",
        template='plotly',
        color_discrete_sequence=px.colors.qualitative.Bold
    )


    # Create a JSON representation of the chart for rendering in the template
    pie_chart2.update_layout(showlegend=False)
    pie_chart_html2 = pie_chart2.to_html(full_html=False)

    # 4th Pie Chart: Are you experiencing any effects of climate change in your area?
    pie_data3 = df['Do you track or calculate your personal carbon footprint?'].value_counts()
    pie_chart3 = px.pie(
        names=pie_data3.index,
        values=pie_data3.values,
        #title="Are you experiencing any effects of Climate Change in your area?",
        template='plotly',
        color_discrete_sequence=px.colors.qualitative.Bold
    )


    # Create a JSON representation of the chart for rendering in the template
    pie_chart3.update_layout(showlegend=False)
    pie_chart_html3 = pie_chart3.to_html(full_html=False)


    # title Which of the following climate change effects are you aware of? Select the relevant column for climate change effects
    climate_effects_column = 'Which of the following climate change effects are you aware of? (Select all that apply)'
    df_clean = df.dropna(subset=[climate_effects_column])
    df_clean[climate_effects_column] = df_clean[climate_effects_column].str.split(',')
    df_exploded = df_clean.explode(climate_effects_column)
    df_exploded[climate_effects_column] = df_exploded[climate_effects_column].str.strip()

    # Count the number of occurrences of each option
    option_counts = df_exploded[climate_effects_column].value_counts()

    # Calculate percentages
    total_responses = option_counts.sum()
    option_percentages = (option_counts / total_responses) * 100

    # Create a bar chart using Plotly
    bar_chart = px.bar(
        x=option_counts.values,
        y=option_counts.index,
        orientation='h',
        labels={'x': 'Count', 'y': 'Climate Change Effects'},
        template='plotly',
        color_discrete_sequence=['#7B3FBC']  # Color: Purple
    )

    # Add text to show counts and percentages on the bars
    bar_chart.update_traces(
        text=[f'{count} ({percent:.1f}%)' for count, percent in zip(option_counts, option_percentages)],
        textposition='auto'
    )
    
    # Disable the legend
    bar_chart.update_layout(showlegend=False)
    
    # Adjust chart layout to resemble the desired look
    bar_chart.update_layout(
        xaxis=dict(tickmode='linear'),
        yaxis_title=None,
        xaxis_title=None,
        height=500,
        margin=dict(l=200)  # Adjust left margin to fit longer labels
    )
    
    # Render the chart as HTML
    bar_chart_html = bar_chart.to_html(full_html=False,config={
        'displayModeBar': False  # This disables the toolbar
    })

    # Pass the chart HTML to the Jinja2 template
    return templates.TemplateResponse("insights.html", {
        "request": request,
        "pie_chart": pie_chart_html,
        "pie_chart2": pie_chart_html2,
        "pie_chart3": pie_chart_html3,
        "bar_chart": bar_chart_html
    })
