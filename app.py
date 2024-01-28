##Setting up the Flask App:
from flask import Flask ,render_template,redirect,url_for,jsonify,request
import pandas as pd

#Flask object Cretion WSGI  
app = Flask(__name__)

# CSV file name
csv_file = 'user_data.csv'
df = pd.read_csv(csv_file)


# Function to read CSV file into a DataFrame
def read_csv():
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['user_id','name', 'Email', 'location'])
        #Index.rename(user_id, *, inplace=True) #Unique ID
    return df

# Function to write DataFrame to CSV file
def write_csv(df):
    df.to_csv(csv_file, index=False)


# Route to store the submited data
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get user data from the form
    user_id = request.form['user_id']
    name = request.form['name']
    email = request.form['email']
    location = request.form['location']
    new_user = pd.DataFrame({'user_id':[user_id],'name': [name], 'Email': [email], 'location': [location]})
    # Read existing CSV data
    existing_data = read_csv()
    updated_data = pd.concat([existing_data, new_user], ignore_index=True)
    write_csv(updated_data)
    return redirect('/')
    
##Retrieve a list of all users 
@app.route('/all_user_details')
def all_user_details():
    user_data= df.to_dict('records')
    print(user_data)
    return render_template('getUserdetails.html',df=user_data)


##Retrieve details of a user by ID
@app.route('/get_user_by_id/<user_id>', methods=['GET'])    
def get_user_by_id(user_id):
    custom_ID = int(user_id)
    user_data = df[df['user_id'] == custom_ID].to_dict('records')
    print(user_data)
    return render_template('getuserbyID.html',df = user_data)


##Retrieve details of a user by name.
@app.route('/user_by_name/<user_name>', methods=['GET'])
def user_by_name(user_name):
    filtered_users = [user for index, user in df.iterrows() if user['name'] == user_name]
    print(filtered_users)  # Add this line for debugging
    return render_template('getusersbyname.html', df=filtered_users)

##Retrieve details of a user by email.
@app.route('/user_by_email/<user_email>',methods = ['GET'])
def user_by_email(user_email):
    user_data = df[df['Email'] == user_email].to_dict('records')
    print(user_data)
    return render_template('getuserbyemail.html', df=user_data)
 
##Retrieve details of users by location.
@app.route('/user_by_location/<user_location>',methods = ['GET'])
def user_by_location(user_location):
    user_data = df[df['location'] == user_location].to_dict('records')
    print(user_data)
    return render_template('grtuserbylocation.html', df=user_data)

"""@app.route('/updated_user_details/<user_id>' , methods = ['POST'])
def update_col(value):
    if pd.notnull(value):
        return 'abc'
    return value
def updated_user_details(user_id):
    df = pd.read_csv(csv_file)
    custom_ID = int(user_id)
    user_data = df[df['user_id'] == custom_ID]
    
    if not user_data.empty:
        for column in df.columns:
            df[column] = df[column].apply(update_col)
            updated_data = df.to_dict('records')
            print(updated_data)
    else:
        print("User not found")

@app.route('/updated_user_details/<user_id>', methods=['GET'])    
def updated_user_details(user_id):
    df = pd.read_csv(csv_file)
    custom_ID = int(user_id)
    user_data = df[df['user_id'] == custom_ID].to_dict('records')
    if user_data:
        user_data = request.form or request.json or request.args
        df.update({
            'name': user_data.get('name', user_data['name']),
            'email': user_data.get('email', user_data['email']),
            'location': user_data.get('location', user_data['location'])
        })
        pd.write_csv(df)
        return jsonify({'message': f'User {user_id} updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404"""






@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Check if the user exists
    user_to_update = df[df['user_id'] == user_id]

    if not user_to_update.empty:
        # Get updated data from the request (form, JSON, or args)
        updated_data = request.form or request.json or request.args

        # Update user data
        user_to_update['name'] = updated_data.get('name', user_to_update['name'].values[0])
        user_to_update['email'] = updated_data.get('email', user_to_update['email'].values[0])
        user_to_update['location'] = updated_data.get('location', user_to_update['location'].values[0])

        # Write the updated DataFrame back to the CSV file
        df.to_csv(csv_file, index=False)

        # Return the updated user data as JSON
        return jsonify({'message': 'User updated successfully', 'updated_data': user_to_update.to_dict(orient='records')})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/Updated_user/<int:user_id>', methods=['GET'])
def Updated_user(user_id):
    # Retrieve user data for a specific user ID
    user_data = df[df['user_id'] == user_id].to_dict(orient='records')
    if user_data:
        return jsonify({'user_data': user_data})
    else:
        return jsonify({'error': 'User not found'}), 404

   
## Delete a user by ID.
@app.route('/delete_user_by_id/<user_id>')
def delete_user_by_id(user_id):
    custom_ID = int(user_id)
    list_user=list(df['user_id'])
    for x in list_user:
        if x == custom_ID:
            list_user.remove(x)
    df = df[df['user_id'].isin(list_user)]
    df.to_csv(csv_file, index=False)
    rem_user = df.to_dict('records')
    print(rem_user)
    return render_template('deletebyid.html', users = rem_user)

# Endpoint to render user data in HTML format
@app.route('/render_users_html', methods=['GET'])
def render_users_html():
    users = pd.read_csv(csv_file)
    return render_template('index.html', users=users)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)







