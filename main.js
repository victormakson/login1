
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-analytics.js";


  const firebaseConfig = {
    apiKey: "AIzaSyBJUg4qlKYMxkeszUxLP-i5liK7h7hogyk",
    authDomain: "login-4bb38.firebaseapp.com",
    projectId: "login-4bb38",
    storageBucket: "login-4bb38.appspot.com",
    messagingSenderId: "53299144859",
    appId: "1:53299144859:web:3dab2d1cd1ab8f70bf7e3e",
    measurementId: "G-ZXKG2TK0XG"
  };

  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
