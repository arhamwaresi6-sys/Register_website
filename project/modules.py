from .extentions import db
from werkzeug.security import generate_password_hash
member_skill = db.Table(
    "member_skill",
    db.Column("member_id", db.Integer, db.ForeignKey("member.id")),
    db.Column("skill_id", db.Integer, db.ForeignKey("skill.id"))
)
class Member(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    salary = db.Column(db.Numeric(10,2))
    password_hash = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date)
    personal_website = db.Column(db.String(100))
    gender = db.Column(db.Enum("male", "female", "other"))
    department_id = db.Column(db.Integer,db.ForeignKey("department.id"))
    experience = db.Column(db.Enum("beginner", "intermediate", "advanced"))
    profile_pic_url = db.Column(db.String(500))
    about = db.Column(db.Text)
    skill_level = db.Column(db.Integer)
    favorite_color = db.Column(db.String(7))
    terms_accepted = db.Column(db.Boolean, default=False, nullable=False)
    @property
    def password(self):
        raise AttributeError("cant read pass")
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

class Department(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    department_name = db.Column(db.String(100),nullable = False)
    members = db.relationship("Member",backref="department")

class Skill(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    skill_name = db.Column(db.String(100),nullable = False)
    members = db.relationship(
        "Member",
        secondary=member_skill,
        lazy=True,
        backref="skills"
)