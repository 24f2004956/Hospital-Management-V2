<template>
    <div class="container mt-4">
        <h2>Edit Profile</h2>

        <div v-if="doctor" class="card p-4 shadow-sm">

            <div class="mb-3">
                <label class="form-label">Name</label>
                <input v-model="doctor.name" class="form-control" />
            </div>

            <div class="mb-3">
                <label class="form-label">Email</label>
                <input v-model="doctor.email" class="form-control" />
            </div>

            <div class="mb-3">
                <label class="form-label">Department</label>
                <select v-model="doctor.department_id" class="form-control">
                    <option v-for="d in departments" :key="d.id" :value="d.id">
                        {{ d.name }}
                    </option>
                </select>
            </div>

            <div class="mb-3">
                <label class="form-label">Experience (Years)</label>
                <input type="number" v-model="doctor.experience_years" class="form-control" />
            </div>

            <div class="mb-3">
                <label class="form-label">about</label>
                <input v-model="doctor.about" class="form-control" />
            </div>

            <div class="mb-3">
                <label class="form-label">profile</label>
                <input v-model="doctor.profile" class="form-control" />
            </div>

            <div class="mb-3">
                <label class="form-label">qualification</label>
                <input v-model="doctor.qualification" class="form-control" />
            </div>

            <div class="mb-3">
                <label class="form-label">contact</label>
                <input v-model="doctor.contact" class="form-control" />
            </div>

            <button class="btn btn-secondary me-2" @click="$router.back()">Back</button>
            <button class="btn btn-success" @click="updateProfile">Save Changes</button>

        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            doctor: null,
            departments: []
        };
    },

    async mounted() {
        const doctor_res = await fetch("/api/doctor/me", {
            headers: { Authorization: "Bearer " + localStorage.getItem("doctorToken") }
        });
        this.doctor = await doctor_res.json();

        const department_res = await fetch("/api/department", {
            headers: { Authorization: "Bearer " + localStorage.getItem("doctorToken") }
        });
        this.departments = await department_res.json();
    },

    methods: {
        async updateProfile() {
            const res = await fetch(`/api/doctor/profile-update`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: "Bearer " + localStorage.getItem("doctorToken")
                },
                body: JSON.stringify(this.doctor)
            });

            const result = await res.json();
            alert(result.message);

            if (res.ok) this.$router.push("/doctor-dashboard");
        }
    }
};
</script>
