db.create_all()
db.session.commit()
Student.query.get  is a method used in SQLAlchemy to retrieve a row from the Student table based on its primary key.
Student.query.filter_by
Loan.query.filter(
                    (Loan.student_id == student_id.data)
                    &
                    # (Loan.returndatetime.is_(None))
                    (Loan.returndatetime.is_(None))
                ).first()

loans = db.relationship('Loan', backref='student', cascade='all,delete')
def make_shell_context():
    return  dict(db=db,Student=Student,Loan=Loan,datetime=datetime)

# When you specify a column as a primary key, this should
# ensure that the column is not null, and unique
# • However, this doesn’t work for integer columns in SQLite
# • As a workaround, set the primary key to True, as usual, but
# also explicitly set unique to True and nullable to false

# Without that, you would have to explicitly do the imports
# everytime you start the shell:
# 1 from app import db
# 2 from app . m o d e l s import S t u d e n t , Loan
# 3 from d a t e t i m e import d a t e t i m e 
