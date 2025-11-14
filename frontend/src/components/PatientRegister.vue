<template>
  <div class="register-page">
    <div class="register-card">
      <div class="register-header">
        <div class="icon-circle">
         <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path
                d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z">
              </path>
            </svg>
        </div>
        <h2>Patient Registration</h2>
      </div>

      <form @submit.prevent="registerPatient" class="register-form">
        <div class="form-group">
          <label for="name">Full Name</label>
          <input type="text" id="name" v-model="name" placeholder="Enter full name" required />
        </div>

        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" v-model="email" placeholder="your@email.com" required />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" placeholder="Create a password" required />
        </div>

        <div v-if="errorMessage" class="message error">{{ errorMessage }}</div>
        <div v-if="successMessage" class="message success">{{ successMessage }}</div>

        <button type="submit" class="btn-register">Register</button>
      </form>

      <p class="login-link">
        Already have an account?
        <a href="/patient-login">Login here</a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
    name: 'PatientRegister',
    data() {
        return {
            name: '',
            email: '',
            password: '',
            errorMessage: null,
            successMessage: null,
        }
    },
    methods: {
        async registerPatient() {
            this.errorMessage = null;
            this.successMessage = null;
            const payload = {
                name: this.name,
                email: this.email,
                password: this.password,
                role: 'patient'
            };
            try {
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const result = await response.json();

                if (!response.ok) {
                    this.errorMessage = result.message ;
                }else{
                    this.successMessage=result.message;
                    alert(result.message);
                    this.$router.push('/patient-login');
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        }
    }
}
</script>

<style scoped>
/* --- Layout --- */
.register-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #d1fae5, #f0fdf4);
  padding: 20px;
}

.register-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
  padding: 30px 35px;
  width: 100%;
  max-width: 420px;
  transition: all 0.3s ease;
}

.register-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 30px rgba(22, 163, 74, 0.2);
}

/* --- Header --- */
.register-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 25px;
}

.icon-circle {
  background-color: #dcfce7;
  padding: 10px;
  border-radius: 50%;
  margin-right: 10px;
}

.register-header h2 {
  font-size: 1.6rem;
  font-weight: 600;
  color: #0d3f21;
}

/* --- Form --- */
.register-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-group label {
  display: block;
  font-weight: 500;
  color: #374151;
  margin-bottom: 6px;
}

.form-group input {
  width: 100%;
  padding: 10px 12px;
  border: 1.5px solid #d1d5db;
  border-radius: 10px;
  font-size: 0.95rem;
  transition: border 0.3s, box-shadow 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #127536;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2);
}

/* --- Messages --- */
.message {
  text-align: center;
  font-size: 0.9rem;
  font-weight: 500;
}

.message.error {
  color: #dc2626;
}

.message.success {
  color: #117a38;
}

/* --- Button --- */
.btn-register {
  background: #1ab653;
  color: white;
  padding: 10px 0;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}

.btn-register:hover {
  background: #177c3c;
  transform: translateY(-1px);
}

/* --- Footer link --- */
.login-link {
  text-align: center;
  margin-top: 20px;
  font-size: 0.9rem;
  color: #4b5563;
}

.login-link a {
  color: #137e3a;
  text-decoration: none;
  font-weight: 600;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
