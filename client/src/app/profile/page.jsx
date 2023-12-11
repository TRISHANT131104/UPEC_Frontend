// 'use client' indicates that this code will run on the client side
"use client";

// Importing necessary React components, hooks, and styles
import React, { useContext } from "react";
import ProfileCard from "@/components/ProfilePageComponents/ProfileCard";
import SkillsCard from "@/components/ProfilePageComponents/SkillsCard";
import StatsCard from "@/components/ProfilePageComponents/StatsCard";
import ProfileDescriptionCard from "@/components/ProfilePageComponents/ProfileDescriptionCard";
import { useQuery } from "@tanstack/react-query";
import HomeContext from "@/context/HomeContext";
import axios from "axios";

// Functional component for the profile page
export default function page() {
  // Destructuring authentication information from HomeContext
  const { auth } = useContext(HomeContext);

  // Query for fetching user profile details using React Query
  const userDetails = useQuery({
    queryKey: ["userProfileDetails"],
    queryFn: () => {
      return fetchUserDetails(auth.user.id);
    },
  });
  
  // Loading state check, display loading message if data is still loading
  if (userDetails.isLoading) {
    return <div>Loading...</div>;
  }
  // Render UI
  return (
    <div className="flex max-md:flex-col background">
      {/* Left column with ProfileCard and StatsCard components */}
      <div className="flex flex-col md:basis-1/3">
        <ProfileCard ele={userDetails} />
        <StatsCard ele={userDetails} />
      </div>
      {/* Right column with ProfileDescriptionCard and SkillsCard components */}
      <div className="flex flex-col md:basis-2/3">
        <ProfileDescriptionCard ele={userDetails} />
        <SkillsCard ele={userDetails} />
      </div>
    </div>
  );
}

// Function to fetch user details using Axios
const fetchUserDetails = (id) => {
  return axios
    .get(`http://103.159.214.229/api/v1/__get__user__data__/${id}`)
    .then((response) => {
      return response.data;
    })
    .catch((err) => {
      alert(err); // Display alert for any error during data fetching
    });
};
