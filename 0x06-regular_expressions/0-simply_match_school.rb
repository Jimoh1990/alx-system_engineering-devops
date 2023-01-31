#!/usr/bin/env ruby
# A regular expression that is simply matching School

input = ARGV[0]

if input.match(/School/)
  puts input.match(/School/)[0]
else
  puts ""
end
