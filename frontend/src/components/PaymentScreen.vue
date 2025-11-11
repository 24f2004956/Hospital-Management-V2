<template>
  <div class="container p-4">
    <h3>Confirm Appointment Payment</h3>

    <div class="card p-3 mt-3">
      <p><strong>Doctor:</strong> {{ doctor.name }}</p>
      <p><strong>Date:</strong> {{ date }}</p>
      <p><strong>Time:</strong> {{ time }}</p>
      <p><strong>Amount to Pay:</strong> ₹{{ fee }}</p>

      <label class="mt-3"><strong>Reason for Appointment:</strong></label>
      <textarea class="form-control" v-model="reason" placeholder="Describe your health issue..." rows="3"></textarea>


      <button class="btn btn-success w-100 mt-3" @click="confirmPayment">
        Pay & Confirm
      </button>

      <button class="btn btn-secondary w-100 mt-2" @click="$router.back()">
        Cancel
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      doctor: {},
      date: this.$route.query.date,
      time: this.$route.query.time,
      fee: this.$route.query.fee,
      doctor_id: this.$route.query.doctor_id,
      reason: ""
    };
  },
  async mounted() {
  const token = localStorage.getItem("patientToken");
  const res = await fetch(`/api/doctor-details/${this.doctor_id}`, {
    headers: { Authorization: `Bearer ${token}` }
  });


  this.doctor = await res.json();
},

  methods: {
    async confirmPayment() {
      const token = localStorage.getItem("patientToken");
      const res = await fetch("/api/appointment", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          doctor_id: this.doctor_id,
          date: this.date,
          time: this.time,
          reason: this.reason,
          payment_status: "paid"
        })
      });

      const data = await res.json();
      alert(data.message);
      this.$router.push("/patient-dashboard");
    }
  }
};
</script>
