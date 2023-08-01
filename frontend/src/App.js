import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css"; // Import the CSS file

function App() {
  const [data, setData] = useState([]);
  const [selectedQuery, setSelectedQuery] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage, setItemsPerPage] = useState(10);
  const [totalPages, setTotalPages] = useState(1);
  const [totalCount, setTotalCount] = useState(0); // Add state for total count
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    fetchData();
  }, [currentPage]);

  const fetchData = () => {
    // Make sure a query option is selected before making the request
    if (!selectedQuery) {
      console.error("Please select a query from the dropdown.");
      return;
    }

    // Calculate the offset to fetch data for the current page
    const offset = (currentPage - 1) * itemsPerPage;

    // Make the backend request with pagination parameters
    axios
      .get(`http://localhost:8000/${selectedQuery}`, {
        params: {
          offset: offset,
          limit: itemsPerPage,
        },
      })
      .then((response) => {
        // Handle the response from the backend here
        console.log(response.data);
        setData(response.data.data); // Update the state with the fetched data
        setTotalCount(response.data.totalCount); // Update the total count
        setTotalPages(Math.ceil(response.data.totalCount / itemsPerPage)); // Update the total pages
        setIsLoading(false); // Set isLoading to false after data is fetched
      })
      .catch((error) => {
        // Handle errors if the request fails
        console.error(error);
        setIsLoading(false); // Set isLoading to false even if an error occurs
      });
  };

  const handleRunQuery = () => {
    // Reset currentPage to 1 when a new query is selected
    setCurrentPage(1);
    // Fetch data from the server
    setIsLoading(true); // Set isLoading to true before fetching data
    fetchData();
  };

  const handleSelectChange = (event) => {
    // Update the state with the selected value from the dropdown
    setSelectedQuery(event.target.value);
  };

  // Function to handle page change
  const handlePageChange = (page) => {
    setIsLoading(true);
    setCurrentPage(page);
  };

  const calculateRowNumber = (rowIndex) => {
    return (currentPage - 1) * itemsPerPage + rowIndex + 1;
  };

  return (
    <div>
      <h1>Data Management Internship</h1>
      <h3>By Haoking Suryanatmaja</h3>
      <div className="query-container">
        <select onChange={handleSelectChange} value={selectedQuery}>
          {/* Dropdown options */}
          <option value="">Select a query</option>
          <option value="q1">1. List the following details of each employee: employee number, last name, first name, sex, and salary</option>
          <option value="q2">2. List first name, last name, and hire date for employees who were hired in 1986</option>
          <option value="q3">3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name</option>
          <option value="q4">4. List the department of each employee with the following information: employee number, last name, first name, and department name</option>
          <option value="q5">5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."</option>
          <option value="q6">6. List all employees in the Sales department, including their employee number, last name, first name, and department name</option>
          <option value="q7">7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name</option>
          <option value="q8">8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name</option>
        </select>
        <button onClick={handleRunQuery}>Run Query</button>
      </div>
      {isLoading ? (
        <div className="loading-container">
          <div className="loading"></div>
        </div>
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th>No</th> {/* Change the header for the row number column to "No" */}
              {data.length > 0 &&
                Object.keys(data[0]).map((column, index) => (
                  <th key={index}>{column}</th>
                ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, rowIndex) => (
              <tr key={rowIndex}>
                <td>{calculateRowNumber(rowIndex)}</td> {/* Display the row number */}
                {Object.values(row).map((value, colIndex) => (
                  <td key={colIndex}>{value}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <div className="page-info">
        Page: {currentPage} / {totalPages} {/* Display current page and total pages */}
      </div>
      <div className="total-rows">
        Total Rows: {totalCount} {/* Display total count of data */}
      </div>
      {/* Pagination controls */}
      <div className="pagination">
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
        >
          Prev
        </button>
        <button
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default App;
