# Open Biz Assignment (Udyam Aadhaar & PAN Validation System)

A complete full-stack application built with **Node.js**, **Express**, **PostgreSQL**, **Prisma**, **React.js**, **Tailwind CSS**, and **Next.js**.  
Deployed on **Vercel** (frontend) and **Render** (backend).  

---

## 🚀 Features

- **Aadhaar & PAN Number Validation**
- **Two-Step Form Submission** (Frontend ↔ Backend Integration)
- **PostgreSQL Database** with Prisma ORM
- **RESTful API** using Express.js
- **Responsive UI** built with Tailwind CSS + Next.js
- **Cross-Origin Communication** (CORS enabled)
- **Production Deployment** on Vercel & Render

---

## 🛠 Tech Stack

**Frontend**
- Next.js (React Framework)
- Tailwind CSS (Styling)
- Axios (API calls)
- Hosted on **Vercel**

**Backend**
- Node.js + Express.js
- Prisma ORM
- PostgreSQL
- Hosted on **Render**

---

## 📂 Project Structure

```plaintext
.
├── backend/                 # Node.js + Express + Prisma API
│   ├── prisma/               # Prisma schema & migrations
│   ├── src/
│   │   ├── routes/           # API Routes (Aadhaar, PAN)
│   │   ├── app.js            # Express app
│   │   └── server.js         # Server entry point
│   └── package.json
│
├── frontend/                # Next.js + Tailwind CSS frontend
│   ├── pages/                # Next.js pages
│   ├── components/           # UI Components
│   └── package.json
│
└── README.md
```
---

## ⚙️ Installation & Setup

```git clone <your-repo-url>
cd <your-repo-folder>
```
---

## ⚙️ Backend Setup
```cd backend
npm install
```
---

## Create a .env file
```
DATABASE_URL="postgresql://<username>:<password>@<host>:<port>/<db>?schema=public"
PORT=5000

```

## Run Prisma migrations

```
npx prisma migrate dev

```

---

## Start Backend
```
npm run dev
```
---
## Start Frontend
```
cd frontend
npm install
```
---

## 🌐 Deployment
--> Frontend (Vercel):
Push your frontend folder to a GitHub repo → Import into Vercel → Deploy.

--> Backend (Render):
Push your backend folder to GitHub → Import into Render → Select Node.js → Set environment variables.

---

## 🧪 Testing
For backend unit tests (Jest + Supertest):
```
cd backend
npm test
```
## Deployment at 
```
openbiz-project.vercel.app
```
---

## ✨ Author
Vasu Sharma
B.Tech CSE | J.C. Bose University
📧 Email: vasu.eit.21cse140@gmail.com
🌐 Portfolio: https://thvasu.vercel.app
