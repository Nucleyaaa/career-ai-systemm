# How to Run the Career AI System

This guide provides step-by-step instructions for running the Career AI System on your local machine.

## 📋 Prerequisites

Before you start, make sure you have the following installed:
- **Python 3.8+** (for the backend)
- **Node.js 16+** and **npm** (for the frontend)
- **Git** (for version control)

## 🚀 Quick Start

### Step 1: Setup Backend (Python/FastAPI)

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server:**
   ```bash
   python run_backend.py
   ```
   
   ✅ **Backend will be running at:** http://localhost:8000
   
   📖 **API Documentation available at:** http://localhost:8000/docs

### Step 2: Setup Frontend (Next.js/React)

1. **Open a new terminal window** (keep backend running)

2. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

3. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

4. **Start the development server:**
   ```bash
   npm run dev
   ```
   
   ✅ **Frontend will be running at:** http://localhost:3000

## 🌐 Access the Application

Once both services are running:

- **Main Application**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🛠️ Development Commands

### Backend Commands (from `/backend` directory)
```bash
# Start backend server
python run_backend.py

# Install new dependencies
pip install package_name
pip freeze > requirements.txt

# Check backend health
curl http://localhost:8000/
```

### Frontend Commands (from `/frontend` directory)
```bash
# Start development server
npm run dev npm run dev npm run dev npm run dev

# Build for production
npm run build

# Start production server
npm start

# Install new dependencies
npm install package_name
```

## 🔍 Troubleshooting

### Common Issues and Solutions

#### Backend Issues

**Issue: ModuleNotFoundError**
```bash
Solution: Make sure you're in the backend directory and virtual environment is activated
cd backend
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

**Issue: Port 8000 already in use**
```bash
Solution: Kill the process using port 8000 or change port in run_backend.py
# Windows: netstat -ano | findstr :8000
# Kill process: taskkill /PID <process_id> /F
```

#### Frontend Issues

**Issue: npm command not found**
```bash
Solution: Install Node.js from https://nodejs.org/
```

**Issue: Port 3000 already in use**
```bash
Solution: Next.js will automatically use the next available port (3001, 3002, etc.)
Or kill the process using port 3000
```

**Issue: Module not found errors**
```bash
Solution: Delete node_modules and reinstall
rm -rf node_modules package-lock.json  # macOS/Linux
rmdir /s node_modules & del package-lock.json  # Windows
npm install
```

## 📂 Project Structure

```
career-ai-systemm/
├── backend/                 # Python FastAPI backend
│   ├── app/                # Application code
│   ├── requirements.txt    # Python dependencies
│   └── run_backend.py      # Backend startup script
├── frontend/               # Next.js React frontend
│   ├── components/         # React components
│   ├── pages/             # Next.js pages
│   ├── package.json       # Node.js dependencies
│   └── ...
├── ai-engine/             # AI/ML models and logic
└── docker-compose.yml     # Docker configuration
```

## 🐋 Alternative: Using Docker

If you prefer using Docker:

```bash
# Build and run all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

## 📝 Environment Variables

### Backend (.env file in `/backend`)
```
# Add any required environment variables here
DATABASE_URL=your_database_url
API_KEY=your_api_key
```

### Frontend (.env.local file in `/frontend`)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🎯 Next Steps After Setup

1. **Test the API**: Visit http://localhost:8000/docs to explore the API endpoints
2. **Explore the Frontend**: Navigate through the application at http://localhost:3000
3. **Check Logs**: Monitor both terminal windows for any errors or issues
4. **Development**: Both servers support hot reloading for development

## 🆘 Need Help?

- Check the console logs in both terminal windows
- Verify all prerequisites are installed correctly
- Ensure no other applications are using ports 3000 or 8000
- Make sure you're running commands from the correct directories

---

**Happy Coding! 🚀**

Last Updated: $(date)