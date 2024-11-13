import React, { useState } from 'react';
import { TextField, Button, Typography } from '@mui/material';
import './css/JobSubmit.css';

const JobSubmit = () => {
  const [jobTitle, setJobTitle] = useState('');
  const [company, setCompany] = useState('');
  const [location, setLocation] = useState('');

  const handleSubmit = () => {
    console.log('Job Title:', jobTitle);
    console.log('Company:', company);
    console.log('Location:', location);
  };

  return (
    <div className="job-submit">
      <Typography variant="h4" className="title">Submit Job Posting</Typography>
      <TextField
        label="Job Title"
        variant="outlined"
        fullWidth
        margin="normal"
        value={jobTitle}
        onChange={(e) => setJobTitle(e.target.value)}
      />
      <TextField
        label="Company"
        variant="outlined"
        fullWidth
        margin="normal"
        value={company}
        onChange={(e) => setCompany(e.target.value)}
      />
      <TextField
        label="Location"
        variant="outlined"
        fullWidth
        margin="normal"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <Button variant="contained" onClick={handleSubmit}>Submit</Button>
    </div>
  );
};

export default JobSubmit;
