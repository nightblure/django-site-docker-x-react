import "./App.css";

import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import NewsList from "./components/NewsList";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/news" element={<NewsList />}>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
