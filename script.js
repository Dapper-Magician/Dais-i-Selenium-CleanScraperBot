document.getElementById('scraping-form').addEventListener('submit', async function (e) {
    e.preventDefault();
  
    const url = document.getElementById('url-input').value;
    const cssSelector = document.getElementById('css-selector-input').value;
    const outputData = document.getElementById('output-data');
    const scrapeButton = document.getElementById('scrape-button');
    const loadingAnimation = document.getElementById('loading-animation');
    const loadingIndicator = document.getElementById('loading-indicator');
    const errorMessage = document.getElementById('error-message');
    
    
    
     // Clear previous error messages
    errorMessage.classList.add('hidden');
    errorMessage.textContent = '';

    try {
        // Call the CleanScraperBot Electron Production backend with the URL and CSS selector
        const scrapedData = await window.backend.scrape(url, cssSelector);

  
    // Display the scraped data on the page
    const outputData = document.getElementById('output-data');
    outputData.textContent = JSON.stringify(scrapedData, null, 2);
    
    } catch (error) {
    // Display error message if an error occurs during scraping
    console.error(error);
    // Handle error, display error message to the user  
    errorMessage.textContent = error.message;
    errorMessage.classList.remove('hidden');
    } finally {
    // Enable the form and hide the loading indicator
    scrapeButton.disabled = false;
    loadingIndicator.classList.add('hidden');
  }
});
    // Visualize the data
    visualizeData(scrapedData);
  });
  
  function visualizeData(data) {
    // Use D3.js to create a data visualization
    // You can add your specific visualization code here
    const chartContainer = document.getElementById('chart');
    
    // Clear previous chart if exists
    chartContainer.innerHTML = '';
  
    // Example: Create a bar chart
    const chartData = Object.entries(data);
  
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const width = 500 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;
  
    const svg = d3.select(chartContainer)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
  
    const x = d3.scaleBand()
      .range([0, width])
      .padding(0.1)
      .domain(chartData.map(d => d[0]));
  
    const y = d3.scaleLinear()
      .range([height, 0])
      .domain([0, d3.max(chartData, d => d[1])]);
  
    svg.append('g')
      .attr('transform', 'translate(0,' + height + ')')
      .call(d3.axisBottom(x));
  
    svg.append('g')
      .call(d3.axisLeft(y));
  
    svg.selectAll('.bar')
      .data(chartData)
      .enter().append('rect')
      .attr('class', 'bar')
      .attr('x', d => x(d[0]))
      .attr('y', d => y(d[1]))
      .attr('width', x.bandwidth())
      .attr('height', d => height - y(d[1]));
  }
  
// Listen for real-time updates from the backend
window.ipcRenderer.on('scraping-update', (event, data) => {
    // Update the GUI with real-time updates from the scraping process
    const updateElement = document.getElementById('scraping-update');
    updateElement.textContent = data;
  });
  
  // Listen for scraping errors from the backend
  window.ipcRenderer.on('scraping-error', (event, errorMessage) => {
    // Display the error message to the user
    const errorElement = document.getElementById('scraping-error');
    errorElement.textContent = errorMessage;    
