import React, {useState} from "react";

const CreateApplicationComponent = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    middleName: "",
    lastName: "",
    dateOfBirth: "",
    gender: "",
    email: "",
    phone: "",
    socialSecurity: "",
    driversLicense: "",
    income: "",
    address: "",
    city: "",
    state: "",
    zipcode: "",
    mailingAddress: "",
    mailingCity: "",
    mailingState: "",
    mailingZipcode: ""
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const {name, value} = e.target;
    setFormData(prevState => ({...prevState, [name]: value}));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    const apiUrl = "http://localhost:8080/api/applicants";
    const token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": token
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        const result = await response.json();
        console.log("Success:", result);
        setMessage("Applicant created successfully.");
      } else {
        const errorResult = await response.json();
        console.error("Error Response:", errorResult);
        setMessage(`Failed to create applicant: ${errorResult.message || response.status}`);
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("An error occurred while submitting the applicant.");
    }
  };

  return (
    <div>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <label>First Name</label>
        <input
          name="firstName"
          value={formData.firstName}
          onChange={handleChange}
          required
        />
        {/* ... other input fields ... */}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default CreateApplicationComponent;
