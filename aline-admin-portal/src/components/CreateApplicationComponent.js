import React, { useState } from 'react';

const CreateApplicationComponent = () => {
  const [formData, setFormData] = useState({}); // Initialize your form data structure

  // Handle form field changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"; // The JWT token
    try {
      const response = await fetch('http://localhost:8080/api/applications', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token,
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        const result = await response.json();
        console.log('Success:', result);
        // Handle success (e.g., display a message or redirect)
      } else {
        console.error('Error Response:', response);
        // Handle HTTP error responses
      }
    } catch (error) {
      console.error('Error:', error);
      // Handle network errors
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Form fields e.g., <input onChange={handleChange} name="fieldName" /> */}
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateApplicationComponent;
