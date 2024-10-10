from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create APIRouter instance
router = APIRouter()

# Set up templates directory
templates = Jinja2Templates(directory="app/templates")

# Route to render the carbon footprint form
@router.get("/greengauge", response_class=HTMLResponse)
async def display_greengauge_form(request: Request):
    return templates.TemplateResponse("greengauge.html", {"request": request})

# Route to calculate the carbon footprint
@router.post("/calculate_greengauge", response_class=HTMLResponse)
async def calculate_greengauge(
    request: Request,
    tv: float = Form(0),
    washing_machine: float = Form(0),
    mobile_charging: float = Form(0),
    kitchen_chimney: float = Form(0),
    lpg_gas: float = Form(0),
    fan: float = Form(0),
    ac: float = Form(0),
    water_heater: float = Form(0),
    wifi_router: float = Form(0),
    water_pump: float = Form(0),
    lights: int = Form(0),
    lights_time: float = Form(0),
    transportation: str = Form(...),
    waste: float = Form(0),
    diet: str = Form(...)
):
    # Emission factors (in kg CO2)
    emission_factors = {
        "tv": 0.09,  # per hour
        "washing_machine": 0.5,  # per hour
        "mobile_charging": 0.01,  # per hour
        "kitchen_chimney": 0.2,  # per hour
        "lpg_gas": 3.0,  # per hour
        "fan": 0.075,  # per hour
        "ac": 1.5,  # per hour
        "water_heater": 2.0,  # per hour
        "wifi_router": 0.02,  # per hour
        "water_pump": 1.0,  # per hour
        "light": 0.06  # per hour per light
    }
    transport_emission_factors = {
        "car": 4.6,
        "bike": 0.5,
        "public": 1.8,
        "walk": 0.0
    }
    diet_emission_factors = {
        "non-vegetarian": 5.0,
        "vegetarian": 3.0,
        "vegan": 2.0
    }
    waste_emission_factor = 1.2  # kg CO2 per kg waste

    # Calculate carbon footprint
    carbon_emission = (
        tv * emission_factors["tv"] +
        washing_machine * emission_factors["washing_machine"] +
        mobile_charging * emission_factors["mobile_charging"] +
        kitchen_chimney * emission_factors["kitchen_chimney"] +
        lpg_gas * emission_factors["lpg_gas"] +
        fan * emission_factors["fan"] +
        ac * emission_factors["ac"] +
        water_heater * emission_factors["water_heater"] +
        wifi_router * emission_factors["wifi_router"] +
        water_pump * emission_factors["water_pump"] +
        lights * lights_time * emission_factors["light"]
    )
    carbon_emission += transport_emission_factors.get(transportation, 0)
    carbon_emission += diet_emission_factors.get(diet, 0)
    carbon_emission += waste * waste_emission_factor

    # Define emission ranges
    emission_ranges = {
        "low": "0 - 15 kg CO2",
        "medium": "15 - 30 kg CO2",
        "high": "30+ kg CO2"
    }

    # Calculation description
    calculation_description = [
        "The carbon footprint is calculated based on the energy usage of various household appliances, transportation mode, diet type, and waste generation.",
        "Each appliance has a specific emission factor (e.g., TV usage, washing machine, air conditioner) which is multiplied by the duration of usage.",
        "Transportation emissions vary based on the type of transport (car, bike, public transport, etc.).",
        "Dietary choices also contribute to the overall emissions, with non-vegetarian diets generally having a higher carbon footprint.",
        "Waste generation adds to the footprint, calculated at 1.2 kg CO2 per kg of waste."
    ]

    # Render result
    return templates.TemplateResponse(
        "greengauge_result.html",
        {
            "request": request,
            "carbon_emission": round(carbon_emission, 2),
            "emission_ranges": emission_ranges,
            "calculation_description": calculation_description
        }
    )