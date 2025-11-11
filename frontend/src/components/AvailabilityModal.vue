<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5)">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title">Available Slots - {{ doctor.name }}</h5>
          <button class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">

          <div v-for="day in groupedAvailability" :key="day.date" class="mb-3">
            <h6 class="fw-bold">{{ day.date }}</h6>

            <div class="d-flex flex-wrap gap-2">
              <button v-for="slot in day.slots" :key="slot.id" class="btn btn-outline-primary btn-sm"
                @click="goToPayment(day.date, slot)">
                {{ slot.start_time.slice(0, 5) }} - {{ slot.end_time.slice(0, 5) }}
                <span v-if="slot.fee && slot.fee > 0" > ₹{{ slot.fee }}</span>
                <span v-else class="text-muted">Free</span>
              </button>

            </div>
          </div>

          <div v-if="groupedAvailability.length === 0" class="text-center text-muted">
            No availability for this doctor.
          </div>

        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["doctor"],
  data() {
    return {
      availability: []
    };
  },
  computed: {
    groupedAvailability() {
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      const nextWeek = new Date();
      nextWeek.setDate(today.getDate() + 7);
      nextWeek.setHours(0, 0, 0, 0);

      const grouped = {};

      this.availability.forEach(slot => {
        const slotDate = new Date(slot.date + "T00:00:00");

        if (slotDate >= today && slotDate <= nextWeek) {
          if (!grouped[slot.date]) {
            grouped[slot.date] = { date: slot.date, slots: [] };
          }
          grouped[slot.date].slots.push(slot);
        }
      });

      // ✅ Convert to array
      const groupedArray = Object.values(grouped);

      // ✅ Sort dates in ascending order
      groupedArray.sort((a, b) => new Date(a.date) - new Date(b.date));

      // ✅ Sort slots inside each day by start time
      groupedArray.forEach(day => {
        day.slots.sort((a, b) => a.start_time.localeCompare(b.start_time));
      });

      return groupedArray;
    }



  },
  async mounted() {
    const token = localStorage.getItem("patientToken");
    const res = await fetch(`/api/availability?doctor_id=${this.doctor.id}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    this.availability = await res.json();
  },
  methods: {
    goToPayment(date, slot) {
      this.$router.push({
        name: "PaymentScreen",
        query: {
          doctor_id: this.doctor.id,
          date,
          time: slot.start_time.slice(0, 5),
          fee: slot.fee
        }
      });
    },

    async book(date, time) {
      const token = localStorage.getItem("patientToken");

      const res = await fetch("/api/appointment", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          doctor_id: this.doctor.id,
          date,
          time,
          reason: "General Checkup"
        })
      });

      const data = await res.json();
      alert(data.message);
      this.$emit("close"); // close modal after booking
    }
  }
};
</script>
