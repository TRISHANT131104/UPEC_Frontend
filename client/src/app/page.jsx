"use client";

// Importing necessary components and libraries
import ProfileCard from "@/components/HomePageComponents/ProfileCard";
import PostCard from "@/components/HomePageComponents/PostCard";
import RecentChatCard from "@/components/HomePageComponents/recentChatCard";
import RecentEvents from "@/components/HomePageComponents/RecentEvents";
import { useContext, useEffect, useState } from "react";
import axios from "axios";

// Importing data from data.json and using it to map the postcards
import data from "./data.json";
import { useQuery } from "@tanstack/react-query";
import HomeContext from "@/context/HomeContext";
import Loader from "@/components/Loader";

// Function to shuffle an array
const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
};

// Function to get a specified number of random elements from an array
const getRandomElements = (array, count) => {
  const shuffledArray = shuffleArray([...array]);
  return shuffledArray.slice(0, count);
};

// Main component for the Home page
export default function Home() {
  // Accessing authentication information from context
  const { auth } = useContext(HomeContext);
  // State to store random elements for display
  let [randomElements, setRandomElements] = useState([]);

  // Function to search posts based on a given search term
  function searchPosts(posts, searchTerm) {
    searchTerm = searchTerm.toLowerCase();
    setRandomElements(
      posts.filter(
        (post) =>
          post.title.toLowerCase().includes(searchTerm) ||
          post.body.toLowerCase().includes(searchTerm)
      )
    );
    return posts.filter(
      (post) =>
        post.title.toLowerCase().includes(searchTerm) ||
        post.body.toLowerCase().includes(searchTerm)
    );
  }

  // useEffect to set initial random elements when the component mounts
  useEffect(() => {
    setRandomElements(getRandomElements(data, 10));
  }, []);

  // Query for fetching user details using React Query
  const userDetails = useQuery({
    queryKey: ["UserDetails"],
    queryFn: () => {
      return fetchUserDetails(auth.user.id);
    },
  });

  console.log(userDetails);

  // Loading state check, display loader if data is still loading
  if (userDetails.isLoading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  console.log(randomElements);

  // Render UI
  return (
    <div className="flex flex-row p-2 sm:p-5 h-screen lg:text-md text-xs">
      <ProfileCard ele={userDetails} />
      <div className="flex flex-col w-[90%] lg:w-1/2 mx-auto">
        {/* Search box above the posts section */}
        <div className="flex gap-2 justify-center">
          <input
            onChange={(e) => {
              if (e.target.value.length == 0 || e.target.value === "") {
                setRandomElements(getRandomElements(data, 10));
              }
            }}
            id="search_input"
            type="text"
            placeholder="Search for Posts/Projects"
            className="w-[70%] h-10 border border-gray-200 rounded-md p-2 shadow-lg"
          />
          <button
            onClick={() => {
              const arr = searchPosts(
                randomElements,
                document.getElementById("search_input").value
              );
              if (arr.length !== 0) {
                setRandomElements((x) => (x = arr));
                randomElements = arr;
              } else {
                setRandomElements(getRandomElements(data, 10));
              }
            }}
            className="w-[10%] h-10 bg-blue-500 rounded-md text-white shadow-lg"
          >
            Search
          </button>
        </div>
        {/* Mapping and rendering post cards */}
        {randomElements.map((post, index) => (
          <div key={index}>
            <PostCard key={post.id} post={post} />
          </div>
        ))}
      </div>
      {/* Hidden section for recent events and chat */}
      <div className="hidden lg:flex flex-col w-1/4">
        <RecentEvents />
        <RecentChatCard />
      </div>
    </div>
  );
}

// Function to fetch user details using Axios
export const fetchUserDetails = async (id) => {
  return axios
    .get(`http://103.159.214.229/api/v1/__get__user__data__/${id}`)
    .then((response) => {
      return response.data;
    })
    .catch((err) => {
      console.log(err);
    });
};
