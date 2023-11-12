"""myCMDB data model."""
from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from mycmdb import db


class Host(db.Model):
    """Class for hosts."""
    __tablename__ = "hosts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    alias: Mapped[str] = mapped_column(unique=True)
    processor_cores: Mapped[Optional[int]]
    ram: Mapped[Optional[int]]
    disk_size: Mapped[Optional[int]]
    os_id: Mapped[Optional[int]] = mapped_column(ForeignKey("os.id"))

    os: Mapped[Optional["OS"]] = relationship(back_populates="hosts")
    interfaces: Mapped[List["Interface"]] = relationship(back_populates="host")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, alias={self.alias})"


class OS(db.Model):
    """Class for OS."""
    __tablename__ = "os"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    distribution: Mapped[Optional[str]]
    version: Mapped[str]

    hosts: Mapped[List["Host"]] = relationship(back_populates="os")

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id}, name={self.name},"
            f" distribution={self.distribution}, version={self.version})"
    )


class Interface(db.Model):
    """Class for interfaces."""
    __tablename__ = "interfaces"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    mac_address: Mapped[Optional[str]]
    ipv4_address: Mapped[Optional[str]]
    ipv4_mask: Mapped[Optional[str]]
    ipv6_address: Mapped[Optional[str]]
    host_id: Mapped[int] = mapped_column(ForeignKey("hosts.id"))

    host: Mapped[Optional["Host"]] = relationship(back_populates="interfaces")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"
