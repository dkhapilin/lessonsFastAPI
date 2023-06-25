from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("email", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

salary = Table(
    "salary",
    metadata,
    Column("current_salary", String),
    Column("salary_increase", TIMESTAMP),
    Column("user_id", Integer, ForeignKey("user.id"))
)