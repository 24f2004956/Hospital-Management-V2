<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                Patient Register
            </div>
            <div class="card-body">
                <form @submit.prevent="registerPatient">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input type="text" v-model="name" class="form-control" id="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="text" v-model="email" class="form-control" id="email" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" v-model="password" class="form-control" id="password" required>
                    </div>
                    <div v-if="errorMessage" class="text-danger" >{{ errorMessage }}</div>
                    <div v-if="successMessage" class="text-success" >{{ successMessage }}</div>
                    <button type="submit" class="btn btn-success">Register</button>
                </form>
            </div>
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
