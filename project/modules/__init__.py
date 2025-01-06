# modules/__init__.py
from .api_integration import fetch_data
from .route_optimizer import optimize_routes
from .emissions_calculator import calculate_emissions
from .user_interface import get_user_input, display_results
from modules import fetch_data, optimize_routes

# modules/__init__.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Modules package initialized.")

# modules/__init__.py
__version__ = "1.0.0"
__author__ = "Aman Yadav"

import modules
print(modules.__version__)  # Outputs: 1.0.0

# modules/__init__.py
def lazy_import_module(name):
    import importlib
    return importlib.import_module(name)

route_optimizer = lazy_import_module('modules.route_optimizer')
