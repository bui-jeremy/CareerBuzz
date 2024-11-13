import React, { useState } from 'react';
import { Typography, Button } from '@mui/material';
import './css/Profile.css';

const Profile = () => {
  const [jobsApplied, setJobsApplied] = useState(0);
  const [contributions, setContributions] = useState(0);

  return (
    <div className="profile">
      <Typography variant="h4" className="title">Profile</Typography>
      <Typography variant="h6">Jobs Applied: {jobsApplied}</Typography>
      <Typography variant="h6">Contributions: {contributions}</Typography>
      <Button variant="contained" onClick={() => setJobsApplied(jobsApplied + 1)}>Apply for Job</Button>
      <Button variant="contained" onClick={() => setContributions(contributions + 1)}>Add Contribution</Button>
    </div>
  );
};

export default Profile;
