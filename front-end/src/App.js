import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // Import the CSS file

function App() {
  const [data, setData] = useState([]);
  const [selectedQuery, setSelectedQuery] = useState(""); // State to store the selected query

  const handleRunQuery = () => {
    // Make sure a query option is selected before making the request
    if (!selectedQuery) {
      console.error("Please select a query from the dropdown.");
      return;
    }

    // Make the backend request
    axios
      .get(`http://localhost:8000/${selectedQuery}`)
      .then((response) => {
        // Handle the response from the backend here
        console.log(response.data);
        setData(response.data); // Update the state with the fetched data
      })
      .catch((error) => {
        // Handle errors if the request fails
        console.error(error);
      });
  };

  const handleSelectChange = (event) => {
    // Update the state with the selected value from the dropdown
    setSelectedQuery(event.target.value);
  };

  return (
    <div>
      <h1>Data Management Internship</h1>
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
      <table className="table">
        <thead>
          <tr>
            {data.length > 0 &&
              Object.keys(data[0]).map((column, index) => (
                <th key={index}>{column}</th>
              ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {Object.values(row).map((value, colIndex) => (
                <td key={colIndex}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
