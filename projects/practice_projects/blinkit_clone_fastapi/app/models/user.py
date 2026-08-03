from sqlalchemy import Column, Integer, String, Boolean, DateTime , ForeignKey 
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship
from app.database.database import Base


class User(Base): 
    ''' this is super admin wil values name , email ,, password_hash is_active , 
            created_at , updated_at.  He is the one who create branches manager's '''

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False, index=True)

    password_hash = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    

class BranchManager(Base):
    ''' this is a branchmanager model, use to store the branch manager info 
        name , email , is_Actove , created_At , branches who are under the manager'''

    __tablename__ = "branch_managers"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False, index=True)

    password_hash = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )   

    # One manager manages one branch
    branch = relationship(
        "Branches",
        back_populates="manager",
        uselist=False
    )

class Branches(Base):
    ''' This model is for branches addressed 
    fields  - name. address , city , pincode , is_active , branch_id ,  manager's of this branch'''
    __tablename__ = 'branches'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
   
    address = Column(String(255), nullable=False)

    city = Column(String(255), nullable=False)

    pincode = Column(String(10), nullable=False)
   
    is_active = Column(Boolean, default=True)
   
    created_at = Column(
           DateTime(timezone=True),
           server_default=func.now()
       )
   
    updated_at = Column(
           DateTime(timezone=True),
           server_default=func.now(),
           onupdate=func.now()
       )
    branch_id = Column(Integer, ForeignKey("branch_managers.id"))

    manager = relationship("BranchManager", back_populates="branch")