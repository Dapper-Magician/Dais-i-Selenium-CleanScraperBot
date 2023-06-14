const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { CleanScraperBot } = require('./cleanscraperbot');

let mainWindow;
let scraperBot;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false, // Allow access to the DOM API in the renderer process   
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile('index.html');

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}
app.whenReady().then(() => {
    createWindow();

        app.on('ready', () => {
            createWindow();
});
        app.on('activate', () => {
            if (mainWindow === null) {
                createWindow();
    }
        app.on('window-all-closed', () => {
            if (process.platform !== 'darwin') {
                app.quit();
  }
});


  }
});

// Handle scraping requests from the renderer process
ipcMain.handle('scrape-data', async (event, { url, cssSelector }) => {
  const scraperBot = new CleanScraperBot();
  scraperBot.onUpdate((data) => {
    mainWindow.webContents.send('scraping-update', data); // Send real-time updates to the GUI
  });
  const scrapedData = await scraperBot.scrape(url, cssSelector);
  return scrapedData;
})} catch (error) {
    mainWindow.webContents.send('scraping-error', error.message); // Send error message to the GUI
    throw error;
  }
});
