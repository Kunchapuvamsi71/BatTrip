// ==========================================
// BatTrip & SpiderRoam
// Authentication JavaScript
// ==========================================

const AUTH_API_URL = window.BATTRIP_API_BASE || "http://127.0.0.1:5000";

// ==========================================
// REGISTER USER
// ==========================================

async function registerUser(name, email, password) {
    try {
        const response = await fetch(`${AUTH_API_URL}/api/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });

        const result = await response.json();
        console.log("Register response:", result);
        return result;
    } catch (error) {
        console.error("Registration error:", error);
        return {
            status: "error",
            message: "Backend is not connected."
        };
    }
}

// ==========================================
// LOGIN USER
// ==========================================

async function loginUser(email, password) {
    try {
        const response = await fetch(`${AUTH_API_URL}/api/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const result = await response.json();
        console.log("Login response:", result);
        return result;
    } catch (error) {
        console.error("Login error:", error);
        return {
            status: "error",
            message: "Backend is not connected."
        };
    }
}

// ==========================================
// PAGE CONNECTION
// ==========================================

document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.getElementById("registerForm");

    if (registerForm) {
        const registerMessage = document.getElementById("registerMessage");

        registerForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirmPassword").value;

            if (password !== confirmPassword) {
                registerMessage.textContent = "Passwords do not match.";
                registerMessage.style.color = "red";
                return;
            }

            registerMessage.textContent = "Registering...";
            registerMessage.style.color = "blue";

            const result = await registerUser(name, email, password);

            if (result.status === "success") {
                registerMessage.textContent = "Registration successful!";
                registerMessage.style.color = "green";
                registerForm.reset();
            } else {
                registerMessage.textContent = result.message || "Registration failed.";
                registerMessage.style.color = "red";
            }
        });
    }

    const loginForm = document.getElementById("loginForm");

    if (loginForm) {
        const loginMessage = document.getElementById("loginMessage");

        loginForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value;

            loginMessage.textContent = "Logging in...";
            loginMessage.style.color = "blue";

            const result = await loginUser(email, password);

            if (result.status === "success") {
                loginMessage.textContent = "Login successful!";
                loginMessage.style.color = "green";

                localStorage.setItem("loggedInUser", JSON.stringify(result.user));

                setTimeout(function () {
                    window.location.href = "profile.html";
                }, 1000);
            } else {
                loginMessage.textContent = result.message || "Invalid email or password.";
                loginMessage.style.color = "red";
            }
        });
    }
});
