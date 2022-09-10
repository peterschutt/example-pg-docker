from typing import Any
from uuid import UUID

from sqlalchemy import Column, Enum, ForeignKey, text
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.model import InProviderDomain

from .types import EntitiesEnum


class Entity(InProviderDomain):
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[Enum] = mapped_column(Enum(EntitiesEnum, create_constraint=False), nullable=False)
    owner_id: Mapped[UUID | None] = mapped_column(ForeignKey("entity.id"), index=True, nullable=True)
    # ryno id is an implementation detail, not to be exposed to clients.
    ryno_id: Mapped[int] = mapped_column(index=True, nullable=True)
    extra: Mapped[dict[str, Any]] = Column(pg.JSONB, nullable=False, server_default=text("'{}'::jsonb"))
