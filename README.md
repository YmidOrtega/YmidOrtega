<!-- Profile Banner: animated signature (adapts to GitHub's light/dark theme) -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-dark.gif" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-light.gif" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-light.gif" alt="Ymid — It's me" width="480" />
  </picture>
</p>

<!-- Language switcher -->
<p align="center">
  <b>English</b> · <a href="https://github.com/YmidOrtega/YmidOrtega/blob/main/README.es.md">Español</a>
</p>

<!-- Typing Intro -->
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?size=22&duration=2800&pause=700&center=true&vCenter=true&width=750&lines=Components+that+cooperate.+Systems+that+come+alive.;I+design+and+build+scalable+backend+systems+and+APIs" alt="Typing SVG" />
  </a>
</p>

<!-- Badges & Links -->
<p align="center">
  <a href="https://www.ymid.me/" target="_blank"><img src="https://img.shields.io/badge/Portfolio-ymid.me-8B0000?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/ymidortega/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Ymid%20Ortega-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:yortegap7920@proton.me"><img src="https://img.shields.io/badge/Email-yortegap7920%40proton.me-6D4AFF?style=for-the-badge&logo=protonmail&logoColor=white"/></a>
  <img src="https://komarev.com/ghpvc/?username=YmidOrtega&style=for-the-badge&color=10b981" alt="views"/>
</p>

---

### About me
- 👋 Backend developer from Colombia. I build Java applications with Spring Boot, virtual threads and SQL/NoSQL databases.
- 🧠 I enjoy understanding how things work under the hood and finding ways to make them more efficient: concurrency, automation and low-latency systems.
- 🌱 I came to software from Environmental Engineering, and haven't stopped learning and building since.
- ☕ Outside the code: science fiction, cycling and languages.

---

### Toolbox
<p align="center">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
  <img src="https://img.shields.io/badge/RocksDB-FF6C37?style=for-the-badge&logo=rocksdb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/JUnit_5-25A162?style=for-the-badge&logo=junit5&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
</p>

---

### Featured projects

<table>
  <tr>
    <!-- PROJECT 1: TitaniumBOE-Sim -->
    <td width="50%" valign="top">
      <h3 align="center">📈 TitaniumBOE-Sim</h3>
      <p align="justify">
        Simulator of Cboe's BOE binary protocol with a matching engine, trading bots, REST API, WebSocket feed and dashboard — all packaged in a single deployable JAR. Each TCP connection runs on its own Java 21 Virtual Thread: 500+ concurrent sessions with P99 latency under 5 ms.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Virtual_Threads-005F87?style=flat-square"/>
        <img src="https://img.shields.io/badge/Javalin-333333?style=flat-square"/>
        <img src="https://img.shields.io/badge/RocksDB-FF6C37?style=flat-square"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/TitaniumBOE-Sim"><b>📂 View repository »</b></a>
      </div>
    </td>
    <!-- PROJECT 2: Clínica -->
    <td width="50%" valign="top">
      <h3 align="center">🏥 Clínica — Hospital Management System</h3>
      <p align="justify">
        Microservices system for managing a health clinic — patients, appointments, admissions and billing, with automatic migrations and an AI medical assistant. Dynamic discovery through Eureka and RSA-256 signed JWT: each service validates with the public key, without sharing secrets.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
        <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>
        <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Clinica"><b>📂 View repository »</b></a>
      </div>
    </td>
  </tr>
  <tr>
    <!-- PROJECT 3: CRUD-Test -->
    <td width="50%" valign="top">
      <h3 align="center">🔐 CRUD-Test — Users API with JWT</h3>
      <p align="justify">
        REST API for users with two-phase registration and stateless JWT authentication, where the user transitions from PENDING to ACTIVE. The partial token lives 15 minutes, is invalidated once consumed and prevents replay attacks in the activation flow; backed by integration tests.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
        <img src="https://img.shields.io/badge/MySQL-005C84?style=flat-square&logo=mysql&logoColor=white"/>
        <img src="https://img.shields.io/badge/Flyway-CC0000?style=flat-square&logo=flyway&logoColor=white"/>
        <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/CRUD-Test"><b>📂 View repository »</b></a>
      </div>
    </td>
    <!-- PROJECT 4: Awaken -->
    <td width="50%" valign="top">
      <h3 align="center">📱 Awaken — Wake-on-LAN Controller</h3>
      <p align="justify">
        Native Android app to wake and shut down devices on the network — Magic Packet (WOL), remote shutdown via SSH and background ICMP ping monitoring. Integrates with the system through Quick Settings Tiles, a home screen widget and push notifications on status change.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white"/>
        <img src="https://img.shields.io/badge/Android_SDK-3DDC84?style=flat-square&logo=android&logoColor=white"/>
        <img src="https://img.shields.io/badge/SSH-000000?style=flat-square"/>
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Awaken-WoL"><b>📂 View repository »</b></a>
      </div>
    </td>
  </tr>
</table>

---

### Metrics & Activity

<div align="center">
  <img src="https://github-readme-stats-fast.vercel.app/api?username=YmidOrtega&show_icons=true&theme=radical" alt="YmidOrtega's GitHub stats" />
</div>

---

<!-- Snake Game -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/YmidOrtega/YmidOrtega/blob/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/YmidOrtega/YmidOrtega/blob/output/github-snake.svg" />
    <img alt="GitHub Snake" src="https://github.com/YmidOrtega/YmidOrtega/blob/output/github-snake.svg" />
  </picture>
</p>

---

### Let's talk
- 💼 **Availability:** Open to freelance projects, technical consulting or just to chat about technology.
- 🌐 **Website:** [ymid.me](https://www.ymid.me/)
- 📨 **Contact:** [yortegap7920@proton.me](mailto:yortegap7920@proton.me)
- 🔗 **LinkedIn:** [linkedin.com/in/ymidortega](https://www.linkedin.com/in/ymidortega/)
