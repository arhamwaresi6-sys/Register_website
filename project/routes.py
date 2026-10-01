from flask import Blueprint,render_template,request,redirect,url_for
from .modules import Member,Department,Skill
from .extentions import db,supabase
from datetime import datetime
main = Blueprint("main",__name__)
@main.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        salary = request.form.get("salary")
        date_of_birth = request.form.get("date_of_birth")
        password = request.form.get("password")
        personal_website = request.form.get("personal_website")
        gender = request.form.get("gender")
        department_id = request.form.get("department")
        experience = request.form.get("experience")
        skill_ids = request.form.getlist("skills")
        file = request.files.get("profile_picture")
        about = request.form.get("about")
        skill_level = request.form.get("skill_level")
        favorite_color = request.form.get("favorite_color")
        terms_accepted = request.form.get("terms_accepted")
        profile_pic_url = None
        if file and file.filename:
            file_path = f"profile_pictures/{file.filename}"
            supabase.storage.from_("New Bucket").upload(
                file=file.read(),
                path = file_path,
                file_options={
                    "content-type":file.content_type
                }
                
            )
            profile_pic_url = supabase.storage \
                .from_("New Bucket") \
                .get_public_url(file_path)
        
        member = Member(
            name = name,
            email = email,
            salary = salary,
            date_of_birth = datetime.strptime(date_of_birth,"%Y-%m-%d").date(),
            password = password,
            personal_website = personal_website,
            gender = gender,
            department_id = department_id,
            experience = experience,
            profile_pic_url=profile_pic_url,
            about = about,
            skill_level = skill_level,
            favorite_color = favorite_color,
            terms_accepted = (
                True if terms_accepted == "on" else False
            )
        )
        db.session.add(member)
        get_skills = db.session.execute(
            db.select(Skill).where(Skill.id.in_(skill_ids))
        ).scalars().all()
        member.skills.extend(get_skills)

        db.session.add(member)
        db.session.commit()
        return redirect(url_for("users"))



    departments = db.session.execute(
            db.select(Department)
        ).scalars().all()
    skills = db.session.execute(
            db.select(Skill)
        ).scalars().all()
    send = {
        "departments" : departments,
        "skills":skills
    }
    return render_template("form.html",**send)
@main.route("/users")
def users():
    return render_template("users.html")


@main.route("/api/users")
def get_users():
    members = db.session.execute(
        db.select(Member)
    ).scalars().all()

    return [
        {
            "name": member.name,
            "id": member.id,
            "email": member.email
        }
        for member in members
    ]
@main.route("/member/<int:id>")
def member(id):
    member = db.session.execute(db.select(Member).where(Member.id == id)).scalars().first()
    return render_template("member.html",member=member)