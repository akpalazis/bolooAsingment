import React, { useState } from 'react';

function MyForm() {
  const [inputValue, setInputValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Send the data to the backend
    try {
      const response = await fetch('http://localhost:5000', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url:inputValue }),
      });

      const data = await response.json();
      console.log(data)
      // Update the state with the submitted value from the backend
      setSubmittedValue(data["short_url"]);
    } catch (error) {
      console.error('Error sending data to the backend:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Enter text:
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
      </form>
      {submittedValue && <p>http://localhost:5000/{submittedValue}</p>
      }
    </div>
  );
}

export default MyForm;
