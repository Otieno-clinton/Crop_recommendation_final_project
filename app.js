const express = require("express");
const app = express();
const port = 3001;
const path = require("path");
const mysql = require("mysql2");
const bodyParser = require("body-parser");
app.use(bodyParser.json());

const pool = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "C@40002284#",
  database: "orders",
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

pool.query("SELECT 1 + 1 AS solution", (error, results) => {
  if (error) {
    console.error("Error connecting to the database:", error);
  } else {
    console.log(
      "Database connected successfully. The solution is: ",
      results[0].solution
    );
  }
});

app.use(express.static(path.join(__dirname, "public")));

app.get("/registration", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "registration.html"));
});
app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "login.html"));
});

app.get("/success", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "success.html"));
});

// Handle registration form submission and insert data into the database
app.post(
  "/registration",
  express.urlencoded({ extended: true }),
  async (req, res) => {
    const { username, contact, email, password } = req.body;

    // Insert data into the new_transcribers table
    const insertQuery = `
      INSERT INTO new_users (name, contact, email,  password)
      VALUES (?, ?, ?, ?)
    `;
    try {
      const [insertResults] = await pool
        .promise()
        .execute(insertQuery, [username, contact, email, password]);
      console.log("User registered successfully:", insertResults);

      res.redirect("/login");
    } catch (error) {
      console.error("Error inserting data:", error);
      res.redirect("/registration");
    }
  }
);

// Handle password reset form submission
app.post("/login", express.urlencoded({ extended: true }), async (req, res) => {
  const { login_email, login_password } = req.body;
  // passwordresetEmail, passwordresetPhone, passwordresetPassword

  // Check if the email and phone_number match a user in the database
  const checkUserQuery = `SELECT * FROM new_users WHERE email = ? AND password = ?`;
  const [userResults] = await pool
    .promise()
    .execute(checkUserQuery, [login_email, login_password]);

  if (userResults.length === 0) {
    res.json({
      error: "Invalid email or password. Please provide correct information.",
    });
    return;
  }
  res.json({ success: "Login successful." });
  // res.redirect('/success');
  try {
  } catch (error) {
    console.error("Error updating password:", error);
    res.status(500).json({ error: "Internal server error." });
  }
});

//start the server
app.listen(port, () => {
  console.log(`server is running on http://localhost:${port}`);
});
