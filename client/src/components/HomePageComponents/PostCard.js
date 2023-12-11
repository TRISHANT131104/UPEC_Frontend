"use client";
import Link from 'next/link';
import React from 'react'
import { useState } from 'react'

export default function PostCard(props) {
  const [name, setName] = useState(props.post.user);
  const [image, setImage] = useState(props.post.profile);
  const [tagline, setTagline] = useState(props.post.designation);
  const [postHeading, setPostHeading] = useState(props.post.title);
  const [postDescription, setPostDescription] = useState(props.post.body);
  const [tags, setTags] = useState(props.post.hashtags);
  const [picture, setPicture] = useState(props.post.picture);
  const [link, setLink] = useState(props.post.link);
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
                <a className="inline-block titleTextDiv" href="#">{name}</a>
              </div>
              <div className="bodyTextDiv">
                {tagline}
              </div>
            </div>
          </div>
        </div>
        <div className="">
          <div className="flex justify-center">
            <Link className="flex" href="#">
              <img className="max-w-full rounded-l-lg"
                src={picture} />
            </Link>
          </div>
        </div>
        <h2 className="titleTextDiv m-5">
          {postHeading}
        </h2>
        <div className="mx-5">
          <p className='bodyTextDiv'>
            {/* slice body to first 100 words */}
            {postDescription.length > 500 ? postDescription.slice(0, 500) + "..." : postDescription}
          </p>
        </div>
        <div className="p-2 sm:p-4 flex flex-wrap items-center">
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
