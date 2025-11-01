<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                Doctor Register
            </div>
            <div class="card-body">
                <form @submit.prevent="registerDoctor">
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
                    <div class="mb-3">
                        <label for="department" class="form-label">Department</label>
                        <select v-model="department_id" class="form-select" id="department" required>
                            <option value="" disabled>Select a department</option>
                            <option v-for="d in departments" :key="d.id" :value="d.id">
                                {{ d.name }}
                            </option>
                        </select>
                    </div>

                    <div v-if="errorMessage" class="text-danger">{{ errorMessage }}</div>
                    <div v-if="successMessage" class="text-success">{{ successMessage }}</div>
                    <button type="submit" class="btn btn-success">Register</button>
                </form>
            </div>
        </div>

    </div>

</template>

<script>
export default {
    name: 'DoctorRegister',
    data() {
        return {
            name: '',
            email: '',
            password: '',
            department_id: '',
            departments: [],
            errorMessage: null,
            successMessage: null,
        }
    },
    methods: {
        async registerDoctor() {
            this.errorMessage = null;
            this.successMessage = null;
            const payload = {
                name: this.name,
                email: this.email,
                password: this.password,
                department_id: this.department_id,
                role: 'doctor'
            };
            try {
                const response = await fetch('/api/doctor', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
                    },
                    body: JSON.stringify(payload)
                });
                const result = await response.json();

                if (!response.ok) {
                    this.errorMessage = result.message;
                } else {
                    this.successMessage = result.message;
                    alert(result.message);
                    this.$router.push('/admin-dashboard');
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        },
        async fetchDepartment(){
            try {
                const response = await fetch('/api/department', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
                    }
                });
                const result = await response.json();
                if (!response.ok) {
                    this.errorMessage = result.message;
                } else {
                    this.departments = result;
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        }
    },
    mounted() {
        this.fetchDepartment();
    }
}
</script>
