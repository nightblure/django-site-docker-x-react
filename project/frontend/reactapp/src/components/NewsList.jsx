import React from "react";
import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const TOKEN = "adbb09381bcc273fdf5a417b89f24ac9e6ea179e";
const AUTH_TOKEN_VALUE = `Token ${TOKEN}`;

const NewsList = () => {
  let [newsList, setNews] = useState([]);

  let getNews = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/news/", {
      headers: {
        "Content-Type": "application/json",
        Authorization: AUTH_TOKEN_VALUE,
      },
      method: "GET",
    });

    let data = await response.json();
    let items = new Map(Object.entries(data));
    let news_list = items.get("results");
    setNews(news_list);
  };

  useEffect(() => {
    getNews();
  }, []);

  return (
    <div>
      {newsList.map((news_element, index) => (
        <div key={index} className="card mb-3">
          <div className="card-header">
            <a href="/#" className="list-group-item list-group-item-action">
              Категория: {news_element.category}
            </a>
          </div>

          <div className="card-body">
            <div className="media d-flex">
              <div className="media-body">
                <h5 className="card-title"> {news_element.title} </h5>
                <div className="card-text">
                  {" "}
                  <div
                    dangerouslySetInnerHTML={{ __html: news_element.content }}
                  />{" "}
                </div>
              </div>
            </div>
          </div>

          <div
            className="card-footer"
            style={{
              flexDirection: "row",
              display: "flex",
              justifyContent: "space-between",
            }}
          >
            <div className="text-muted">
              {" "}
              {news_element.user_str}, {news_element.created_at}{" "}
            </div>
            <span
              style={{ float: "right" }}
              className="badge rounded-pill text-bg-primary"
            >
              {" "}
              {news_element.views_count} views{" "}
            </span>
          </div>
        </div>
      ))}
    </div>
  );
};

export default NewsList;
