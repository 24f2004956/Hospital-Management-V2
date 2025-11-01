<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                Admin Login
            </div>
            <div class="card-body">
                <form @submit.prevent="loginadmin">
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="text" v-model="email" class="form-control" id="email" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" v-model="password" class="form-control" id="password" required>
                    </div>
                    <div v-if="errorMessage" class="text-danger" >{{ errorMessage }}</div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>
        </div>

    </div>

</template>

<script>
export default {
    name: 'AdminLogin',
    data() {
        return {
            email: '',
            password: '',
            errorMessage: null,
        }
    },
    methods: {
        async loginadmin() {
            // Handle login logic here
            this.errorMessage = null;
            const payload = {
                email: this.email,
                password: this.password
            };
            try {
                const response = await fetch('/api/login', {
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
                    alert('Login successful');
                    localStorage.setItem('adminToken', result.token);
                    this.$router.push('/admin-dashboard');
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        }
    }
}
</script>
