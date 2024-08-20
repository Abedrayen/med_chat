<template>
  <LayoutPatient>
    <template #content>
      <div class="page">
        <div class="top">
          <div class="text-box">
            <h2 class="title text-3xl font-extrabold text-black inline">
              Bienvenue chez
              <span class="Primary-p-500 inline">DOCARE</span>
            </h2>
            <h3 class="text">
              Votre espace dédié au bien-être et à la santé Explorez nos services exceptionnels
              conçus pour vous accompagner vers une vie équilibrée
            </h3>
          </div>

          <!-- Search  Bar -->
          <div class="recherche">
            <RechercheDoc />
          </div>

          <!-- Stats Bar -->
          <div
            class="stats-bar bg-[#00b9e3] py-6 flex justify-around items-center rounded-b-lg mt-auto"
          >
            <div class="stat text-center text-white">
              <h3 class="text-4xl font-bold">24/7</h3>
              <p class="text-lg">Support</p>
            </div>
            <div class="stat text-center text-white">
              <h3 class="text-4xl font-bold">100+</h3>
              <p class="text-lg">Doctors Available</p>
            </div>
            <div class="stat text-center text-white">
              <h3 class="text-4xl font-bold">1M</h3>
              <p class="text-lg">Patients</p>
            </div>
          </div>
        </div>

        <!-- ChatIcon Bar -->
        <ChatbotIcon @click="toggleChat" />
        
        <!-- Chatbot Component -->
        <Chatbot :isOpen="isChatbotOpen" @close-chat="toggleChat" />
      </div>
    </template>
  </LayoutPatient>
</template>

<script>
import RechercheDoc from '@/components/organisms/RechercheDoc/RechercheDoc.vue'
import LayoutPatient from '@/components/templates/layouts/LayoutPatient/LayoutPatient.vue'
import ChatbotIcon from '@/components/icons/ChatbotIcon.vue'
import Chatbot from '@/components/chatBot/ChatbotInterface.vue'

export default {
  components: {
    LayoutPatient,
    RechercheDoc,
    ChatbotIcon,
    Chatbot,
  },
  data() {
    return {
      isChatbotOpen: false,
    };
  },
  methods: {
    toggleChat() {
      this.isChatbotOpen = !this.isChatbotOpen;
    },
  },
};
</script>
<style>
.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--Dark-Dark-7, #d1d5db);
}
.top {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 30px;
  background: #f3f4f6;
  padding: 0;
}
.Primary-p-500 {
  color: #00b9e3;
}
.text-box {
  padding: 60px;
  margin-top: auto;
  gap: 10px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.recherche {
  margin-left: 50px;
  position: relative;
  width: 803px;
  left: 20px;
  padding-left: 20px;
  width: 100%;
  max-width: 803px;
}
.title {
  width: auto;
  color: var(--grey-grey-darken-4, #212121);
  font-family: Raleway;
  font-size: 70px;
  font-weight: 700;
  line-height: 72px;
  margin-bottom: 20px;
}

.text {
  color: var(--Text-Primary-Text-Color, #637381);
  font-family: Raleway;
  font-size: 24px;
  font-style: normal;
  font-weight: 600;
  line-height: 125%;
  width: 803px;
  height: 53px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 30px;
  margin-top: 20px;
}

.stats-bar {
  position: relative;
  background-color: #00b9e3;
  border-radius: 0px 0px 30px 30px;
  padding: 20px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 100%;
}

@media (max-width: 640px) {
  .title {
    font-size: 2.5rem;
    line-height: 1.2;
    margin-top: 80px;
  }
}
</style>
