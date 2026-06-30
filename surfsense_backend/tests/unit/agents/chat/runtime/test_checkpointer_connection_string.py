from unittest.mock import patch

from app.agents.chat.runtime.checkpointer import get_postgres_connection_string


def test_get_postgres_connection_string_maps_asyncpg_ssl_to_psycopg_sslmode():
    url = (
        "postgresql+asyncpg://postgres:secret@db.example.supabase.co:5432/postgres"
        "?ssl=require"
    )
    with patch("app.agents.chat.runtime.checkpointer.config") as mock_config:
        mock_config.DATABASE_URL = url
        assert get_postgres_connection_string() == (
            "postgresql://postgres:secret@db.example.supabase.co:5432/postgres"
            "?sslmode=require"
        )
