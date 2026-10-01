from flask_sqlalchemy import SQLAlchemy
import os
from supabase import create_client, Client
supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)
db = SQLAlchemy()