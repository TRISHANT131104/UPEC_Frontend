// Setting the environment to use client-side rendering
"use client";

// Importing Link and React from Next.js, and useState from React
import Link from 'next/link';
import React from 'react'
import { useState } from 'react'

// Functional component for rendering a post card
export default function PostCard(props) {
  // State variables to manage post details
  const [name, setName] = useState(props.post.user);
  const [image, setImage] = useState(props.post.profile);
  const [tagline, setTagline] = useState(props.post.designation);
  const [postHeading, setPostHeading] = useState(props.post.title);
  const [postDescription, setPostDescription] = useState(props.post.body);
  const [tags, setTags] = useState(props.post.hashtags);
  const [picture, setPicture] = useState(props.post.picture);
  const [link, setLink] = useState(props.post.link);

  // JSX structure for rendering the post card
  return (
    <a className="flex justify-center" href={link}>
      <article className="my-5 break-inside flex flex-col bg-clip-border h-max w-full sm:w-[90%] mx-auto card !p-0">
        <div className="flex items-center p-3 justify-between bg-white rounded-t-md">
          <div className="flex">
            <Link className="inline-block" href="#">
              <img className="rounded-full max-w-none w-12 h-12 xl:w-16 xl:h-16" src={image} />
            </Link>
            <div className="flex flex-col mx-2 justify-center">
              <div className="flex">
                {/* Link to the user's profile */}
                <a className="inline-block titleTextDiv" href="#">{name}</a>
              </div>
              <div className="bodyTextDiv">
                {/* Tagline or designation of the user */}
                {tagline}
              </div>
            </div>
          </div>
        </div>
        <div className="">
          <div className="flex justify-center">
            <Link className="flex" href="#">
              {/* Image associated with the post */}
              <img className="max-w-full rounded-l-lg"
                src={picture} />
            </Link>
          </div>
        </div>
        <h2 className="titleTextDiv m-5">
          {/* Title or heading of the post */}
          {postHeading}
        </h2>
        <div className="mx-5">
          <p className='bodyTextDiv'>
            {/* Displaying a truncated version of the post description */}
            {postDescription.length > 500 ? postDescription.slice(0, 500) + "..." : postDescription}
          </p>
        </div>
        <div className="p-2 sm:p-4 flex flex-wrap items-center">
          {/* Mapping over tags to display them */}
          {tags.map((tag,index) => (
            <div key={index} className="bg-gray-100 rounded-full px-3 py-1 text-xs font-semibold text-gray-600 mr-2 mb-2">
              {tag}
            </div>
          ))}
        </div>
      </article>
    </a>
  )
}
