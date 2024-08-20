<script>
import axios from 'axios';

export default {
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      messages: [
        { content: "Welcome! How can I assist you today?", sender: "bot" },
      ],
      userInput: "",
    };
  },
  methods: {
    closeChat() {
      this.$emit('close-chat');
    },
    async sendMessage() {
      if (this.userInput.trim() !== "") {
        // Add the user's message to the messages array
        this.messages.push({ content: this.userInput, sender: "user" });

        // Send the message to the backend
        try {
          const response = await axios.post("http://localhost:5000/chatbot/", {
            query: this.userInput,
          });

          // Add the bot's response to the messages array
          this.messages.push({ content: response.data.response, sender: "bot" });

        } catch (error) {
          console.error("Error communicating with the chatbot backend:", error);
        }

        // Clear the input field
        this.userInput = "";
      }
    },
  },
};
</script>
