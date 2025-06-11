import psycopg2
import psycopg2.extras
db_name="postgres"
db_user="postgres.ykmdauexsqwnylxqzzzn"
db_password="Supabasewhatsapp06"
port="5432", 
db_host="aws-0-ap-south-1.pooler.supabase.com"

def SafeHood_db():
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password,  port="5432",  host=db_host)
    cur = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT "Name", "Email", phone_number, type_of_issue, location, "Description" FROM public."SafeHood"')
    safehood=cur.fetchall()
    cur.close()
    connect.close()
    return safehood

def reports(name, email, phone_number, type_of_issue, location, description, photo):
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password,  port="5432",  host=db_host)
    cur = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('INSERT INTO public."SafeHood"("Name", "Email", phone_number, type_of_issue, location, "Description", photo) VALUES (%s, %s, %s, %s, %s, %s, %s)', (name, email, phone_number, type_of_issue, location, description, photo))
    connect.commit()
    cur.close()
    connect.close()
    