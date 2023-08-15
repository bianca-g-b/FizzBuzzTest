# FizzBuzzTest

Instructions on how to run the application:

Make sure you have installed the following on your machine:
Python3
Node.js
npm

Clone the repository to your local machine:
https://github.com/bianca-g-b/FizzBuzzTest.git

Navigate to the backend folder.
cd python_backend

Install the required python packages:
pip install -r requirements.txt

Run the backend server:
python3 main.py

Open a new terminal window.
Navigate to the frontend folder.

cd react_frontend

Install the required node packages:
npm install

Run the frontend server:
npm start

Open a browser and navigate to http://localhost:3000/



Security measures and considerations:

Unfortunately, I didn't have enought time to implement login and authentication as I would have wanted to.

I was planning to implement user registration and login using JWT tokens.
Upon successful login, a token containing user_id and expiration time of 1 hour would be generated.
I also wanted to have protected routes that would only allow access to certain pages only if the user was logged in. These routes would be protected by requiring a valid token.
The backend server would verify the token and its validity before allowing access.
Then I would have implemented a logout function that would invalidate the token and log the user out.

For a larger-scale project, I would consider using third party authentication services such Supabase (which I have used before) or Auth0.

I believe two-factor authentication is also a good security measure to implement.