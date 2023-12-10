"use client";
import ProfileCard from "@/components/HomePageComponents/ProfileCard"
import PostCard from "@/components/HomePageComponents/PostCard"
import RecentChatCard from "@/components/HomePageComponents/recentChatCard"
import RecentEvents from "@/components/HomePageComponents/RecentEvents"
import { useEffect, useState } from "react"

// import data.json and use its data to map the postcards

import data from "./data.json"

const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
};

const getRandomElements = (array, count) => {
  const shuffledArray = shuffleArray([...array]);
  return shuffledArray.slice(0, count);
};

export default function Home() {

  const [randomElements, setRandomElements] = useState([]);

  useEffect(() => {
    setRandomElements(getRandomElements(data, 10));
  }, []);

  return (
    <div className="flex flex-row p-2 sm:p-5 h-screen lg:text-md text-xs">
      <ProfileCard/>
      <div className="flex flex-col w-[90%] lg:w-1/2 mx-auto">
        {/* Make a search box above the posts section*/}
        <div className="flex gap-2 justify-center">
          <input type="text" placeholder="Search for Posts/Projects" className="w-[70%] h-10 border border-gray-200 rounded-md p-2 shadow-lg"/>
          <button className="w-[10%] h-10 bg-blue-500 rounded-md text-white shadow-lg">Search</button>
        </div>
        {randomElements.map((post) => (
          <PostCard key={post.id} post={post}/>
        ))}
      </div>
      <div className="hidden lg:flex flex-col w-1/4">
          <RecentEvents/>
          <RecentChatCard/>
      </div>
    </div>
  )
}
