import React, { useState } from 'react';
import { TextField, Button, MenuItem, Select, FormControl, InputLabel, Typography } from '@mui/material';
import './css/JobForm.css';

const pathways = [
  "Software Engineering",
  "Cybersecurity",
  "Data Science and Analytics",
  "Cloud Computing and DevOps",
  "Mobile Development",
  "Web Development",
  "Product Management",
  "Embedded Systems and Hardware",
  "Game Development",
  "Database and Network Engineering"
];

const JobForm = () => {
  const [email, setEmail] = useState('');
  const [selectedTracks, setSelectedTracks] = useState([]);

  const handleSubmit = () => {
    console.log('Email:', email);
    console.log('Selected Tracks:', selectedTracks);
  };

  return (
    <div className="job-form">
      <Typography variant="h4" className="title">CareerBuzz - Internships</Typography>
      <TextField
        label="Enter your email"
        variant="outlined"
        fullWidth
        margin="normal"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <FormControl fullWidth margin="normal">
        <InputLabel>Preferred Tracks</InputLabel>
        <Select
          multiple
          value={selectedTracks}
          onChange={(e) => setSelectedTracks(e.target.value)}
          label="Preferred Tracks"
          renderValue={(selected) => selected.join(', ')}
        >
          {pathways.map((track) => (
            <MenuItem key={track} value={track}>
              {track}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <Button variant="contained" onClick={handleSubmit}>Submit</Button>
    </div>
  );
};

export default JobForm;
