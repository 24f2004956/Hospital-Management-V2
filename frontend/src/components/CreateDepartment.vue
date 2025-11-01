<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                Create Department
            </div>
            <div class="card-body">
                <form @submit.prevent="createDepartment">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input type="text" v-model="name" class="form-control" id="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="form-label">Description</label>
                        <textarea v-model="description" class="form-control" id="description" rows="3" required></textarea>
                    </div>
                    <div v-if="errorMessage" class="text-danger">{{ errorMessage }}</div>
                    <div v-if="successMessage" class="text-success">{{ successMessage }}</div>
                    <button type="submit" class="btn btn-success">Create</button>
                </form>
            </div>
        </div>

    </div>

</template>

<script>
export default {
    name: 'CreateDepartment',
    data() {
        return {
            name: '',
            description: '',
            errorMessage: null,
            successMessage: null,
        }
    },
    methods: {
        async createDepartment() {
            this.errorMessage = null;
            this.successMessage = null;
            const payload = {
                name: this.name,
                description: this.description 
            };
            try {
                const response = await fetch('/api/department', {
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
       
    }, 
}
</script>
